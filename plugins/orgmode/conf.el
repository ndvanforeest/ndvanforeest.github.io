(use-package org-special-block-extras
  :ensure t
  :demand t
  :hook (org-mode . org-special-block-extras-mode))

; (require 'org-special-block-extras)

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
