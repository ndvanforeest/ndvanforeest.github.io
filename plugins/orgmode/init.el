(defvar bootstrap-version)
(let ((bootstrap-file
       (expand-file-name "straight/repos/straight.el/bootstrap.el" user-emacs-directory))
      (bootstrap-version 5))
  (unless (file-exists-p bootstrap-file)
    (with-current-buffer
        (url-retrieve-synchronously
         "https://raw.githubusercontent.com/raxod502/straight.el/develop/install.el"
         'silent 'inhibit-cookies)
      (goto-char (point-max))
      (eval-print-last-sexp)))
  (load bootstrap-file nil 'nomessage))
(setq package-enable-at-startup nil)

(straight-use-package 'use-package)
(setq straight-use-package-by-default t)

(use-package htmlize
  :ensure t)

(use-package org-special-block-extras
  :ensure t
  ;; All relevant Lisp functions are prefixed ‘o-’; e.g., `o-docs-insert'.
  :hook (org-mode . org-special-block-extras-mode)
  :custom
    (o-docs-libraries
     '("~/org-special-block-extras/documentation.org")
     "The places where I keep my ‘#+documentation’"))



(require 'org)
(require 'ox-html)
(require 'org-special-block-extras)

;;; Add any custom configuration that you would like to 'conf.el'.
(setq nikola-use-pygments t
      org-export-with-toc nil
      org-export-with-section-numbers nil
      org-startup-folded 'showeverything)

(org-defblock details (title "Details"
              background-color "#e5f5e5" title-color "green")
   (pcase backend
     (`latex (concat (pcase (substring background-color 0 1)
                       ("#" (format "\\definecolor{osbe-bg}{HTML}{%s}" (substring background-color 1)))
                       (_ (format "\\colorlet{osbe-bg}{%s}" background-color)))
                     (pcase (substring title-color 0 1)
                       ("#" (format "\\definecolor{osbe-fg}{HTML}{%s}" (substring title-color 1)))
                       (_ (format "\\colorlet{osbe-fg}{%s}" title-color)))
                     (format "\\begin{quote}
                              \\begin{tcolorbox}[colback=osbe-bg,colframe=osbe-fg,title={%s},sharp corners,boxrule=0.4pt]
                                   %s
                               \\end{tcolorbox}
                \\end{quote}" title contents)))
     (_ (format "<details class=\"code-details\"
                 style =\"padding: 0.6em;
                          background-color: %s;
                          border-radius: 15px;
                          color: hsl(157 75% 20%);
                          font-size: 1em;
                          box-shadow: 0.05em 0.1em 5px 0.01em  #00000057;\">
                  <summary>
                    <strong>
                      <font face=\"Courier\" size=\"3\" color=\"%s\">
                         %s
                      </font>
                    </strong>
                  </summary>
                  %s
               </details>" background-color title-color title contents))))


(org-defblock box (title "" background-color nil shadow nil)
  (pcase backend
    (`latex
     (apply #'concat
            `("\\begin{tcolorbox}[title={" ,title "}"
              ",colback=" ,(pp-to-string (or background-color 'red!5!white))
              ",colframe=red!75!black, colbacktitle=yellow!50!red"
              ",coltitle=red!25!black, fonttitle=\\bfseries,"
              "subtitle style={boxrule=0.4pt, colback=yellow!50!red!25!white}]"
              ,contents
              "\\end{tcolorbox}")))
    ;; CSS syntax: “box-shadow: specification, specification, ...”
    ;; where a specification is of the shape “[inset] x_offset y_offset [blur [spread]] color”.
    (_ (-let [haze (lambda (left right deep-right deep-left)
                     (format "width: 50%%; margin: auto; box-shadow: %s"
                             (thread-last (list (cons right      "8px 6px 13px 8px %s")
                                                (cons left       "-16px 12px 20px 16px %s")
                                                (cons deep-right "48px 36px 71px 28px %s")
                                                (cons deep-left  "-48px -20px 71px 28px %s"))
                               (--filter (car it))
                               (--map (format (cdr it) (car it)))
                               (s-join ","))))]
         (format "<div style=\"%s\"> <h3>%s</h3> %s </div>"
                 (s-join ";" `( "padding: 0.5em;"
                               ,(format "background-color: %s" (org-subtle-colors (format "%s" (or background-color "green"))))
                               "border-radius: 15px"
                               "font-size: 1em"
                               ,(when shadow
                                  (cond
                                   ((equal shadow t)
                                    (funcall haze "hsl(60, 100%, 50%)" "hsl(1, 100%, 50%)" "hsl(180, 100%, 50%)" nil))
                                   ((equal shadow 'inset)
                                    (funcall haze "inset hsl(60, 100%, 50%)" "inset hsl(1, 100%, 50%)" "inset hsl(180, 100%, 50%)" nil))
                                   ((or (stringp shadow) (symbolp shadow))
                                    (format "box-shadow: 10px 10px 20px 0px %s; width: 50%%; margin: auto" (pp-to-string shadow)))
                                   ((json-plist-p shadow)
                                    (-let [(&plist :left X :right Y :deep-right Z :deep-left W) shadow]
                                      (funcall haze X Y Z W)))
                                   (:otherwise (-let [(X Y Z W) shadow]
                                        (funcall haze X Y Z W)))))))
                 title contents)))))

(org-defblock exercise (title nil)
  (org-thread-blockcall raw-contents
    (box title)))

(org-defblock solution (title "Solution")
  (org-thread-blockcall raw-contents
    (details title :title-color "red")))


(org-defblock hint (title "Hint")
  (org-thread-blockcall raw-contents
    (details title))) ; :title-color "red")))



;;; Macros

;; Load Nikola macros
(setq nikola-macro-templates
      (with-current-buffer
          (find-file
           (expand-file-name "macros.org" (file-name-directory load-file-name)))
        (org-macro--collect-macros)))

;;; Code highlighting
(defun org-html-decode-plain-text (text)
  "Convert HTML character to plain TEXT. i.e. do the inversion of
     `org-html-encode-plain-text`. Possible conversions are set in
     `org-html-protect-char-alist'."
  (mapc
   (lambda (pair)
     (setq text (replace-regexp-in-string (cdr pair) (car pair) text t t)))
   (reverse org-html-protect-char-alist))
  text)

;; Use pygments highlighting for code
(defun pygmentize (lang code)
  "Use Pygments to highlight the given code and return the output"
  (with-temp-buffer
    (insert code)
    (let ((lang (or (cdr (assoc lang org-pygments-language-alist)) "text")))
      (shell-command-on-region (point-min) (point-max)
                               (format "pygmentize -f html -l %s" lang)
                               (buffer-name) t))
    (buffer-string)))

(defconst org-pygments-language-alist
  '(("asymptote" . "asymptote")
    ("awk" . "awk")
    ("c" . "c")
    ("console" . "console")
    ("c++" . "cpp")
    ("cpp" . "cpp")
    ("clojure" . "clojure")
    ("css" . "css")
    ("d" . "d")
    ("emacs-lisp" . "scheme")
    ("F90" . "fortran")
    ("gnuplot" . "gnuplot")
    ("groovy" . "groovy")
    ("haskell" . "haskell")
    ("java" . "java")
    ("js" . "js")
    ("julia" . "julia")
    ("latex" . "latex")
    ("lisp" . "lisp")
    ("makefile" . "makefile")
    ("matlab" . "matlab")
    ("mscgen" . "mscgen")
    ("ocaml" . "ocaml")
    ("octave" . "octave")
    ("perl" . "perl")
    ("picolisp" . "scheme")
    ("python" . "python")
    ("r" . "r")
    ("ruby" . "ruby")
    ("sass" . "sass")
    ("scala" . "scala")
    ("scheme" . "scheme")
    ("sh" . "sh")
    ("shell-session" . "shell-session")
    ("sql" . "sql")
    ("sqlite" . "sqlite3")
    ("tcl" . "tcl"))
  "Alist between org-babel languages and Pygments lexers.
lang is downcased before assoc, so use lowercase to describe language available.
See: http://orgmode.org/worg/org-contrib/babel/languages.html and
http://pygments.org/docs/lexers/ for adding new languages to the mapping.")

;; Override the html export function to use pygments
(defun org-html-src-block (src-block contents info)
  "Transcode a SRC-BLOCK element from Org to HTML.
CONTENTS holds the contents of the item.  INFO is a plist holding
contextual information."
  (if (org-export-read-attribute :attr_html src-block :textarea)
      (org-html--textarea-block src-block)
    (let ((lang (org-element-property :language src-block))
          (code (org-element-property :value src-block))
          (code-html (org-html-format-code src-block info)))
      (if nikola-use-pygments
          (progn
            (unless lang (setq lang ""))
            (pygmentize (downcase lang) (org-html-decode-plain-text code)))
        code-html))))

;; Export images with custom link type
(defun org-custom-link-img-url-export (path desc format)
  (cond
   ((eq format 'html)
    (format "<img src=\"%s\" alt=\"%s\"/>" path desc))))
(org-add-link-type "img-url" nil 'org-custom-link-img-url-export)

;; Export images with built-in file scheme
(defun org-file-link-img-url-export (path desc format)
  (cond
   ((eq format 'html)
    (format "<img src=\"/%s\" alt=\"%s\"/>" path desc))))
(org-add-link-type "file" nil 'org-file-link-img-url-export)

;; Support for magic links (link:// scheme)
(org-link-set-parameters
  "link"
  :export (lambda (path desc backend)
             (cond
               ((eq 'html backend)
                (format "<a href=\"link:%s\">%s</a>"
                        path (or desc path))))))

;; Export function used by Nikola.
(defun nikola-html-export (infile outfile)
  "Export the body only of the input file and write it to
specified location."
  (with-current-buffer (find-file infile)
    (org-macro-replace-all nikola-macro-templates)
    (org-html-export-as-html nil nil t t)
    (write-file outfile nil)))
