
(cl:in-package :asdf)

(defsystem "aruco_controlled_bot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MarkerPosition" :depends-on ("_package_MarkerPosition"))
    (:file "_package_MarkerPosition" :depends-on ("_package"))
  ))