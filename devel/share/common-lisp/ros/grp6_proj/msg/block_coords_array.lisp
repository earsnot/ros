; Auto-generated. Do not edit!


(cl:in-package grp6_proj-msg)


;//! \htmlinclude block_coords_array.msg.html

(cl:defclass <block_coords_array> (roslisp-msg-protocol:ros-message)
  ((coords
    :reader coords
    :initarg :coords
    :type (cl:vector grp6_proj-msg:block_coords)
   :initform (cl:make-array 0 :element-type 'grp6_proj-msg:block_coords :initial-element (cl:make-instance 'grp6_proj-msg:block_coords))))
)

(cl:defclass block_coords_array (<block_coords_array>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <block_coords_array>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'block_coords_array)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name grp6_proj-msg:<block_coords_array> is deprecated: use grp6_proj-msg:block_coords_array instead.")))

(cl:ensure-generic-function 'coords-val :lambda-list '(m))
(cl:defmethod coords-val ((m <block_coords_array>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader grp6_proj-msg:coords-val is deprecated.  Use grp6_proj-msg:coords instead.")
  (coords m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <block_coords_array>) ostream)
  "Serializes a message object of type '<block_coords_array>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'coords))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'coords))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <block_coords_array>) istream)
  "Deserializes a message object of type '<block_coords_array>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'coords) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'coords)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'grp6_proj-msg:block_coords))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<block_coords_array>)))
  "Returns string type for a message object of type '<block_coords_array>"
  "grp6_proj/block_coords_array")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'block_coords_array)))
  "Returns string type for a message object of type 'block_coords_array"
  "grp6_proj/block_coords_array")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<block_coords_array>)))
  "Returns md5sum for a message object of type '<block_coords_array>"
  "8b5f64b5842ecf35ee87d85a0105c1ad")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'block_coords_array)))
  "Returns md5sum for a message object of type 'block_coords_array"
  "8b5f64b5842ecf35ee87d85a0105c1ad")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<block_coords_array>)))
  "Returns full string definition for message of type '<block_coords_array>"
  (cl:format cl:nil "block_coords[] coords~%================================================================================~%MSG: grp6_proj/block_coords~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'block_coords_array)))
  "Returns full string definition for message of type 'block_coords_array"
  (cl:format cl:nil "block_coords[] coords~%================================================================================~%MSG: grp6_proj/block_coords~%float32 x~%float32 y~%float32 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <block_coords_array>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'coords) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <block_coords_array>))
  "Converts a ROS message object to a list"
  (cl:list 'block_coords_array
    (cl:cons ':coords (coords msg))
))
