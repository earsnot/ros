;; Auto-generated. Do not edit!


(when (boundp 'grp6_proj::block_coords_array)
  (if (not (find-package "GRP6_PROJ"))
    (make-package "GRP6_PROJ"))
  (shadow 'block_coords_array (find-package "GRP6_PROJ")))
(unless (find-package "GRP6_PROJ::BLOCK_COORDS_ARRAY")
  (make-package "GRP6_PROJ::BLOCK_COORDS_ARRAY"))

(in-package "ROS")
;;//! \htmlinclude block_coords_array.msg.html


(defclass grp6_proj::block_coords_array
  :super ros::object
  :slots (_coords ))

(defmethod grp6_proj::block_coords_array
  (:init
   (&key
    ((:coords __coords) (let (r) (dotimes (i 0) (push (instance grp6_proj::block_coords :init) r)) r))
    )
   (send-super :init)
   (setq _coords __coords)
   self)
  (:coords
   (&rest __coords)
   (if (keywordp (car __coords))
       (send* _coords __coords)
     (progn
       (if __coords (setq _coords (car __coords)))
       _coords)))
  (:serialization-length
   ()
   (+
    ;; grp6_proj/block_coords[] _coords
    (apply #'+ (send-all _coords :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; grp6_proj/block_coords[] _coords
     (write-long (length _coords) s)
     (dolist (elem _coords)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; grp6_proj/block_coords[] _coords
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _coords (let (r) (dotimes (i n) (push (instance grp6_proj::block_coords :init) r)) r))
     (dolist (elem- _coords)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get grp6_proj::block_coords_array :md5sum-) "8b5f64b5842ecf35ee87d85a0105c1ad")
(setf (get grp6_proj::block_coords_array :datatype-) "grp6_proj/block_coords_array")
(setf (get grp6_proj::block_coords_array :definition-)
      "block_coords[] coords
================================================================================
MSG: grp6_proj/block_coords
float32 x
float32 y
float32 z

")



(provide :grp6_proj/block_coords_array "8b5f64b5842ecf35ee87d85a0105c1ad")


