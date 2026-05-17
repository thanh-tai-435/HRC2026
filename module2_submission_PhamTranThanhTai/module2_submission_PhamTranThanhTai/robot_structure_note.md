# Robot Structure Note — Walker S2
Người thực hiện: Pham Tran Thanh Tai
URDF: /home/ubuntu/Downloads/WalkerS2-Model/walker_s2_description/urdf/s2/s2.urdf
Script: scripts/list_urdf_structure.py → output/urdf_note.txt
Robot name (URDF): walker_s2_description
Tổng: 33 links, 32 joints (30 revolute + 2 fixed)

---

## 1. Robot Root
| Thông tin | Giá trị | Nguồn |
|-----------|---------|-------|
| USD prim path | /Root/Ref_Xform/Ref | main.py → RobotArticulation() |
| Robot name trong code | walkerS2 | main.py |
| Position | [0.7, -0.2, 0.9] | Part_Sorting.yaml |
| Rotation | [0, 0, 90] | Part_Sorting.yaml |

---

## 2. Waist / Torso
| Joint | Type | Parent → Child | Limit (rad) |
|-------|------|----------------|-------------|
| waist_yaw_joint | revolute | base_link → waist_yaw_link | [-2.8274, 2.8274] |
| waist_pitch_joint | revolute | waist_yaw_link → waist_pitch_link | [-1.5707, 0.6108] |

---

## 3. Head
| Joint | Type | Parent → Child | Limit (rad) |
|-------|------|----------------|-------------|
| head_yaw_joint | revolute | waist_pitch_link → head_yaw_link | [-1.658, 1.658] |
| head_pitch_joint | revolute | head_yaw_link → head_pitch_link | [-0.7854, 0.5236] |

---

## 4. Left Arm (vai → cổ tay)
| STT | Joint | Parent → Child | Limit (rad) |
|-----|-------|----------------|-------------|
| 1 | L_shoulder_pitch_joint | waist_pitch_link → L_shoulder_pitch_link | [-2.8623, 2.8623] |
| 2 | L_shoulder_roll_joint | L_shoulder_pitch_link → L_shoulder_roll_link | [-1.885, 0.1222] |
| 3 | L_shoulder_yaw_joint | L_shoulder_roll_link → L_shoulder_yaw_link | [-2.9322, 2.9322] |
| 4 | L_elbow_roll_joint | L_shoulder_yaw_link → L_elbow_roll_link | [-2.6529, 0.0349] |
| 5 | L_elbow_yaw_joint | L_elbow_roll_link → L_elbow_yaw_link | [-2.9322, 2.9322] |
| 6 | L_wrist_pitch_joint | L_elbow_yaw_link → L_wrist_pitch_link | [-1.658, 1.658] |
| 7 | L_wrist_roll_joint | L_wrist_pitch_link → L_wrist_roll_link | [-2.0245, 2.0245] |
| — | L_sixforce_joint (fixed) | L_wrist_roll_link → **L_sixforce_link** | — |

**End-effector: L_sixforce_link**

---

## 5. Right Arm (vai → cổ tay)
| STT | Joint | Parent → Child | Limit (rad) |
|-----|-------|----------------|-------------|
| 1 | R_shoulder_pitch_joint | waist_pitch_link → R_shoulder_pitch_link | [-2.8623, 2.8623] |
| 2 | R_shoulder_roll_joint | R_shoulder_pitch_link → R_shoulder_roll_link | [-1.885, 0.1222] |
| 3 | R_shoulder_yaw_joint | R_shoulder_roll_link → R_shoulder_yaw_link | [-2.9322, 2.9322] |
| 4 | R_elbow_roll_joint | R_shoulder_yaw_link → R_elbow_roll_link | [-2.6529, 0.0349] |
| 5 | R_elbow_yaw_joint | R_elbow_roll_link → R_elbow_yaw_link | [-2.9322, 2.9322] |
| 6 | R_wrist_pitch_joint | R_elbow_yaw_link → R_wrist_pitch_link | [-1.658, 1.658] |
| 7 | R_wrist_roll_joint | R_wrist_pitch_link → R_wrist_roll_link | [-2.0245, 2.0245] |
| — | R_sixforce_joint (fixed) | R_wrist_roll_link → **R_sixforce_link** | — |

**End-effector: R_sixforce_link**

---

## 6. Legs (không dùng trong thi)
| Nhóm | Joints (6 mỗi chân) |
|------|---------------------|
| Left | L_hip_roll/yaw/pitch, L_knee_pitch, L_ankle_pitch/roll |
| Right | R_hip_roll/yaw/pitch, R_knee_pitch, R_ankle_pitch/roll |

---

## 7. End-Effector & Gripper
| | Left | Right |
|-|------|-------|
| End-effector | L_sixforce_link | R_sixforce_link |
| Xác minh từ | teleop.py comment "sixforce_link yaw=-π/2" | same |
| TCP offset Task 1 | [0.0, 0.0, 0.0] | [0.0, 0.0, 0.0] |
| TCP offset Task 3/4 | [0.0, 0.0, 0.22] | [0.0, 0.0, 0.22] |
| Gripper open | left_gripper = +1.0 | right_gripper = +1.0 |
| Gripper close | left_gripper = -1.0 | right_gripper = -1.0 |

---

## 8. Teleop Action Space (14 dims — teleop_config.py)
| Index | Tên | Ý nghĩa |
|-------|-----|---------|
| 0 | left_delta_x | Tay trái delta X |
| 1 | left_delta_y | Tay trái delta Y |
| 2 | left_delta_z | Tay trái delta Z |
| 3 | left_delta_rx | Tay trái delta Rx |
| 4 | left_delta_ry | Tay trái delta Ry |
| 5 | left_delta_rz | Tay trái delta Rz |
| 6 | right_delta_x | Tay phải delta X |
| 7 | right_delta_y | Tay phải delta Y |
| 8 | right_delta_z | Tay phải delta Z |
| 9 | right_delta_rx | Tay phải delta Rx |
| 10 | right_delta_ry | Tay phải delta Ry |
| 11 | right_delta_rz | Tay phải delta Rz |
| 12 | left_gripper | Gripper trái |
| 13 | right_gripper | Gripper phải |

---

## 9. Câu hỏi còn lại
- [ ] 4 gripper joints tên cụ thể là gì? (không có trong s2.urdf)
- [ ] Camera prim path đầy đủ trong USD stage?
- [ ] Chân có bị lock trong simulation không?
