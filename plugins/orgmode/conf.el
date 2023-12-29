(require 'package)
(setq package-user-dir (expand-file-name "./.packages"))
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("org"       . "http://orgmode.org/elpa/")
                         ("elpa" . "https://elpa.gnu.org/packages/")))

(package-initialize)
(unless (package-installed-p 'use-package)
  (package-install 'use-package))
(require 'use-package)

(use-package org-special-block-extras
  :ensure t
  :hook (org-mode . org-special-block-extras-mode)
  ;; All relevant Lisp functions are prefixed ‘o-’; e.g., `o-docs-insert'.
  :custom
    (o-docs-libraries
     '("~/org-special-block-extras/documentation.org")
     "The places where I keep my ‘#+documentation’"))


(require 'org-special-block-extras)

(org-defblock details (title "Solution")
   (pcase backend
     (`latex (format "\\begin{solution}
                                   %s
                \\end{solution}" contents))
     (_ (format "<details class=\"code-details\"
                 style =\"padding: 1em;
                          background-color: %s;
                          box-shadow: 0.05em 0.1em 5px 0.01em  #00000057;\">
                  <summary>
                    <strong>
                      <font face=\"Courier\" size=\"3\" color=\"%s\">
                         %s
                      </font>
                    </strong>
                  </summary>
                  %s
               </details>" "green" "black" title contents))))


(org-defblock solution
  (title "Solution" reprimand "Did you actually try? Maybe see the ‘hints’ above!"
   really "Solution, for real")
  "Show the answers to a problem, but with a reprimand in case no attempt was made."
  (org-thread-blockcall raw-contents
                    ;(details really)
                    ;(box reprimand)
                    (details)))
