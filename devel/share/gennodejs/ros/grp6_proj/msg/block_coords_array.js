// Auto-generated. Do not edit!

// (in-package grp6_proj.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let block_coords = require('./block_coords.js');

//-----------------------------------------------------------

class block_coords_array {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.coords = null;
    }
    else {
      if (initObj.hasOwnProperty('coords')) {
        this.coords = initObj.coords
      }
      else {
        this.coords = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type block_coords_array
    // Serialize message field [coords]
    // Serialize the length for message field [coords]
    bufferOffset = _serializer.uint32(obj.coords.length, buffer, bufferOffset);
    obj.coords.forEach((val) => {
      bufferOffset = block_coords.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type block_coords_array
    let len;
    let data = new block_coords_array(null);
    // Deserialize message field [coords]
    // Deserialize array length for message field [coords]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.coords = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.coords[i] = block_coords.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 12 * object.coords.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'grp6_proj/block_coords_array';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8b5f64b5842ecf35ee87d85a0105c1ad';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    block_coords[] coords
    ================================================================================
    MSG: grp6_proj/block_coords
    float32 x
    float32 y
    float32 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new block_coords_array(null);
    if (msg.coords !== undefined) {
      resolved.coords = new Array(msg.coords.length);
      for (let i = 0; i < resolved.coords.length; ++i) {
        resolved.coords[i] = block_coords.Resolve(msg.coords[i]);
      }
    }
    else {
      resolved.coords = []
    }

    return resolved;
    }
};

module.exports = block_coords_array;
