
(cl:in-package :asdf)

(defsystem "grp6_proj-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "block_coords" :depends-on ("_package_block_coords"))
    (:file "_package_block_coords" :depends-on ("_package"))
    (:file "block_coords_array" :depends-on ("_package_block_coords_array"))
    (:file "_package_block_coords_array" :depends-on ("_package"))
  ))