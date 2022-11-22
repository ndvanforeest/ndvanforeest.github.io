;; Init file to use with the orgmode plugin.

;; Load org-mode
;; Requires org-mode v8.x

(setq user-init-file (or load-file-name (buffer-file-name)))
(setq user-emacs-directory (file-name-directory user-init-file))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; set custom-file to write into a separate place

(setq custom-file (concat user-emacs-directory ".custom.el"))
(when (file-readable-p custom-file) (load custom-file))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; configure melpa (and other repos if needed)

(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(setq package-enable-at-startup nil)
(package-initialize)

(unless (package-installed-p 'use-package)
 (package-refresh-contents)
 (package-install 'use-package))

;; (eval-when-compile
;;  (require 'use-package))

(use-package org-special-block-extras
  :ensure t
  :hook (org-mode . org-special-block-extras-mode))

(use-package htmlize
  :ensure t)

;; (eval-when-compile
;;  (require 'use-package))

(require 'org)
(require 'ox-html)
; (require 'org-special-block-extras) ; niet nodig

;;; Custom configuration for the export.

;;; Add any custom configuration that you would like to 'conf.el'.
(setq nikola-use-pygments t
      org-export-with-toc nil
      org-export-with-section-numbers nil
      org-startup-folded 'showeverything)

;; Load additional configuration from conf.el
(let ((conf (expand-file-name "conf.el" (file-name-directory load-file-name))))
  (if (file-exists-p conf)
      (load-file conf)))

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
    (format "<img src=\"%s\" alt=\"%s\"/>" path desc))))
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

(org-defblock solution (title "Solution") (title-color "red")
              (pcase backend (`latex (format "\\begin{%s} %s \\end{%s}" (downcase title) contents (downcase title)))
                     (_ (format "<details class=\"code-details\"
                 style =\"padding: 1em;
                          background-color: #e5f5e5;
                          /* background-color: pink; */
                          border-radius: 15px;
                          color: hsl(157 75% 20%);
                          font-size: 0.9em;
                          box-shadow: 0.05em 0.1em 5px 0.01em  #00000057;\">
                  <summary>
                    <strong>
                      <font face=\"Courier\" size=\"3\" color=\"%s\">
                         %s
                      </font>
                    </strong>
                  </summary>
                  %s
               </details>" title-color title contents))))

(org-defblock hint   (title "Hint") (title-color "green")
  (org--blockcall solution title :title-color title-color raw-contents))

;; (org-defblock exercise (title "Exercise") ()
;;      (pcase backend (`latex (format "\\begin{exercise} %s \\end{exercise}" contents))
;;         (_ (org--blockcall box title raw-contents))))

(org-defblock exercise (title "Exercise") ()
   (pcase backend (`latex (format "\\begin{exercise} %s \\end{exercise}" contents))
    (_  (apply #'concat `("<div style=\"padding: 1em; background-color: "
             ,(org-subtle-colors (format "green"))
             ";border-radius: 15px; font-size: 0.9em"
             "; box-shadow: 0.05em 0.1em 5px 0.01em #00000057;\">"
             "<h3>" ,title "</h3>"
            , contents "</div>")))))

(org-defblock exercise (title "Exercise") ()
   (pcase backend (`latex (format "\\begin{exercise} %s \\end{exercise}" contents))
    (_  (apply #'concat `("<div style=\"padding: 1em; background-color: "
             ,(org-subtle-colors (format "green"))
             ";border-radius: 15px; font-size: 0.9em"
             "; box-shadow: 0.05em 0.1em 5px 0.01em #00000057;\">"
             ,(concat  "xercise" contents)
            , "</div>")))))

(org-defblock newthought () ()
  (format (if (equal backend 'html)
            "<strong style=\"font-variant: all-small-caps;\">%s</strong>"
            "\\newthought{%s}")
          contents))
