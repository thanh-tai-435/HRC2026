# Câu hỏi chưa rõ — Module 2
Người thực hiện: Pham Tran Thanh Tai

---

## Q1 — Camera prim path chính xác
Bối cảnh: README có 4 cameras (head_left, head_right, wrist_left, wrist_right).
Đã kiểm tra: URDF s2.urdf không có camera link rõ ràng.
Chưa rõ: Prim path đầy đủ trong USD stage là gì?
Cần làm: Chạy list_usd_prims.py trên s2_v1.usd.

## Q2 — Gripper joints tên cụ thể
Bối cảnh: README nói 20-dim = 14 arm + 4 gripper joints + 2 gripper commands.
Đã kiểm tra: s2.urdf không có gripper joint nào.
Chưa rõ: 4 gripper joints nằm ở file nào? s2_v1.usd hay file riêng?

## Q3 — Teleop nhận command qua cơ chế nào
Bối cảnh: lerobot_record.py set robot_action_to_send=None khi robot.name=="walkerS2".
Đã kiểm tra: WalkerS2KeyboardTeleop.get_action() trả về delta EE.
Chưa rõ: Robot nhận command thực sự qua physics callback nào?

## Q4 — Conveyor speed
Bối cảnh: Conveyor_Sorting.yaml không có field velocity/speed.
Chưa rõ: Tốc độ băng chuyền set ở đâu? Trong USD hay SceneBuilder?

## Q5 — compensation_matrix trong main.py
Bối cảnh: main.py có ma trận 4x4 hardcode cho CoordinateTransform.
Chưa rõ: Ma trận này calibrate cái gì? Fixed offset hay đo thực nghiệm?
