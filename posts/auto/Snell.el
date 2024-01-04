(TeX-add-style-hook
 "Snell"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "a4paper")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10")
   (LaTeX-add-labels
    "sec:org90dd070"
    "sec:orgc58b389"
    "sec:org331af17"
    "snell-eq1"
    "sec:orga257d9b"
    "sec:orgd5f6921"
    "sec:org5faee49"
    "sec:org623508b"
    "eq:snelleq:2"
    "sec:orgfbddb4e"))
 :latex)

