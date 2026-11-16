# 参与贡献 Prodev SLAM Jazzy

感谢您对本项目的关注与支持，欢迎参与贡献！

## 如何贡献

1. Fork 本仓库并将其克隆（Clone）到本地：
2. 为您的新功能或问题修复创建一个新分支：
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. 进行代码修改，并使用 Docker 在本地完成构建与测试：
   ```bash
   bash scripts/docker_run.sh --build --gui
   ```
4. 确保您的代码符合项目现有的风格与规范。
5. 如果您的更改涉及用户可见的功能或行为变化，请同步更新 CHANGELOG.md 和 CHANGELOG_CN.md。
6. 提交（Commit）您的更改，并编写清晰、具有描述性的提交信息。
7. 将分支推送（Push）到您的 Fork 仓库，并向本仓库的 main 分支发起 Pull Request（PR）。

## 开发工作流

- 新功能开发请使用 feature/* 命名的分支。
- Bug 修复请使用 fix/* 命名的分支。
- 保持每次提交（Commit）专注且原子化（单次提交只做一件事）。
- 提交信息可使用英文或中文编写，但需保持简洁、准确且具有描述性。

## 代码规范

- Python：遵循 PEP 8 编码规范。
- C++：遵循 ROS 2 官方代码风格指南。
- Launch 文件：保持参数显式声明，并为非直观的复杂逻辑添加清晰注释。

## 问题反馈

如果您发现了 Bug 或有新功能建议，请使用仓库提供的模板创建 Issue 进行反馈。

## 开源协议

向本项目提交代码贡献，即表示您同意您的贡献内容将遵循本项目所采用的同一开源协议进行授权。