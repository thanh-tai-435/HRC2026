# Code Reading Note — HRC2026 Baseline
Người thực hiện: Pham Tran Thanh Tai
Repo: GlobalHumanoidRobotChallenge_2026_Baseline

---

## 1. Entry Points
| Script | File | Mục đích |
|--------|------|---------|
| Simulation (IK) | Ubtech_sim/main.py | Chạy grasp tự động |
| Teleoperate | src/lerobot/scripts/lerobot_teleoperate.py | Điều khiển keyboard |
| Record | src/lerobot/scripts/lerobot_record.py | Ghi dataset |
| Train | src/lerobot/scripts/lerobot_train.py | Train policy |
| Eval | src/lerobot/scripts/lerobot_eval.py | Đánh giá policy |

## Lệnh record mẫu (từ lerobot_record.py)
```bash
/isaac-sim/python.sh -m lerobot.scripts.lerobot_record \
    --robot.type=walker_s2_sim \
    --robot.headless=false \
    --teleop.type=walker_s2_keyboard \
    --dataset.root=/workspace/datasets/task4/ \
    --dataset.repo_id=liberow/task4_08 \
    --dataset.num_episodes=10 \
    --dataset.single_task="packing box" \
    --dataset.video=true \
    --dataset.push_to_hub=false
```

---

## 2. Folder quan trọng
| Folder | Nội dung |
|--------|---------|
| Ubtech_sim/ | Isaac Sim entry, config, scene/robot/grasp |
| Ubtech_sim/config/ | 4 YAML config cho 4 task |
| src/lerobot/scripts/ | teleop, record, train, eval |
| src/lerobot/teleoperators/walker_s2_keyboard/ | Keyboard teleop Walker S2 |
| src/lerobot/robots/walker_s2_sim/ | Robot wrapper trong sim |
| assets/resources/ | USD: robot, scene, objects |

---

## 3. Data Flow

### Pipeline Simulation (main.py)
Part_Sorting.yaml
→ load_config()
→ SimulationApp + open_stage(scene_usd)
→ World(physics_dt=1/60, rendering_dt=1/20)
→ SceneBuilder.build_all() + scatter parts
→ physics settle 2.0s
→ RobotArticulation("/Root/Ref_Xform/Ref")
→ initialize_ik(s2.urdf) + CoordinateTransform
→ GraspPlanner.compute_grasp_target(part_poses)
→ physics callbacks 60Hz:
robot_control_callback → control_dual_arm_ik()
score_input_record_callback → get_target_object_transforms()
camera_images_callback → DataLogger
→ poses.csv + camera_data.hdf5

### Pipeline Teleop/Record (lerobot_record.py)
keyboard input (evdev/pynput)
→ WalkerS2KeyboardTeleop.get_action()
→ action {left/right delta x/y/z/rx/ry/rz, gripper}
→ robot callback → IK → joint commands
→ world.step()
→ LeRobotDataset.add_frame(obs, action, task)
→ dataset.save_episode()

---

## 4. Năm file quan trọng nhất
| File | Vai trò | Class/Function chính |
|------|---------|---------------------|
| Ubtech_sim/main.py | Entry simulation, IK grasp loop | RobotArticulation, GraspPlanner |
| src/lerobot/scripts/lerobot_record.py | Ghi dataset episode | record(), record_loop() |
| src/lerobot/teleoperators/walker_s2_keyboard/teleop.py | Keyboard control | WalkerS2KeyboardTeleop, get_action() |
| src/lerobot/teleoperators/walker_s2_keyboard/teleop_config.py | Keymap, action space | WalkerS2KeyboardTeleopConfig |
| src/lerobot/scripts/lerobot_train.py | Training pipeline | train(), update_policy() |

---

## 5. Observation & Action
### Teleop Action (14 dims)
```python
action = {
    "left_delta_x/y/z/rx/ry/rz": float,  # EE delta tay trái
    "right_delta_x/y/z/rx/ry/rz": float, # EE delta tay phải
    "left_gripper": float,   # +1=open, -1=close
    "right_gripper": float,
}
```
### Policy State Space: 20 dims
- 14 arm joints (7 per arm) + 4 gripper joints + 2 gripper commands
- Nguồn: README "20-dimensional state space"

---

## 6. Lưu ý quan trọng
- walkerS2 robot_action_to_send = None trong teleop
  → robot nhận command qua physics callback, không qua send_action()
- assets/ là git submodule từ Hugging Face
- Dataset format: LeRobotDataset V3.0, video 4 cameras
