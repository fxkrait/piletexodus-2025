;; siteGenerator.el

;; Generate a basic HTML export

;; pre-tear down
;; https://www.gnu.org/software/emacs/manual/html_node/elisp/Create_002fDelete-Dirs.html
(delete-directory "web" t)

;; create a director for output
(make-directory "web")


(setq sg/audioPath "../../feeds/melody/files/webm_96k/")

(defun sg/create-html-orig ()
  (concat
      "This is\n"
       "a multi\n"
       "line\n"
       "docstring")
  )


(defun 1i ()
"    "
  )


(defun 2i ()
(concat (1i) (1i))
  )

(defun sg/create-html ()
  (concat
   "<!DOCTYPE html>\n"
   "<html>\n"
   (1i) "<body>\n"
   (concat (2i) "<audio controls preload=\"none\"><source src=\"feeds/melody/files/webm_96k/" "AUDIO_FILE_NAME_HERE" "\" type=\"audio/webm\"></audio>\n")
   (1i) "</body>\n"
   "</html>")
  )

(sg/create-html)

(f-write-text (sg/create-html) 'utf-8 "web/test.txt")




(setq
 2025-calendar-days
 (list
  (cons "01" 31)
  (cons "02" 28)
  (cons "03" 31)
  (cons "04" 30)
  (cons "05" 31)
  (cons "06" 30)
  (cons "07" 31)
  (cons "08" 31)
  (cons "09" 30)
  (cons "10" 31)
  (cons "11" 30)
  (cons "12" 31)))

(alist-get "01" 2025-calendar-days 999 nil 'string-equal)

