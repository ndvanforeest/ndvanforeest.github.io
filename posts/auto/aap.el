(TeX-add-style-hook
 "aap"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "pythontex"
    "pgfplots"))
 :latex)

