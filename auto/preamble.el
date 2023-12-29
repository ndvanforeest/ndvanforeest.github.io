(TeX-add-style-hook
 "preamble"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "english")))
   (add-to-list 'LaTeX-verbatim-environments-local "minted")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "a4wide"
    "babel"
    "mathpazo"
    "hyperref"
    "mathtools"
    "amsthm"
    "amssymb"
    "amsmath"
    "tikz"
    "cleveref"
    "minted")
   (TeX-add-symbols
    '("nvf" 1)
    '("abs" 1)
    '("cov" 1)
    '("VV" 2)
    '("V" 1)
    '("EE" 2)
    '("E" 1)
    '("P" 1)
    '("min" 1)
    '("max" 1)
    '("d" 1)
    '("Unif" 1)
    '("Poi" 1)
    '("Norm" 1)
    '("NBin" 1)
    '("Geo" 1)
    '("DUnif" 1)
    '("FS" 1)
    '("Beta" 1)
    '("Bern" 1)
    '("Exp" 1)
    "R"
    "given"
    "F"
    "iid")
   (LaTeX-add-amsthm-newtheorems
    "exercise"
    "remark"
    "theorem"
    "solution"
    "hint"))
 :latex)

