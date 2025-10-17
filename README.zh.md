# 动态路径管理器

[![Python版本](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![许可证](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![构建状态](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/dynamic-path-manager)

**语言**: [English](README.md) | [简体中文](README.zh.md)

一个用于临时添加和移除 `sys.path` 中路径的 Python 上下文管理器。当你需要从不同目录动态导入模块而不永久污染 Python 路径时，这特别有用。

## 特性

- 🚀 **简单的上下文管理器**: 易于使用的上下文管理器接口
- 🧹 **自动清理**: 退出上下文时自动移除路径
- 🔄 **模块缓存管理**: 清除模块缓存以防止冲突
- 🛡️ **安全**: 只移除由管理器添加的路径
- 📦 **轻量级**: 无外部依赖
- 🐍 **Python 3.7+**: 兼容现代 Python 版本

## 安装

```bash
pip install dynamic-path-manager
```

或从源码安装：

```bash
git clone https://github.com/yourusername/dynamic-path-manager.git
cd dynamic-path-manager
pip install -e .
```

## 快速开始

```python
from dynamic_path_manager import DynamicPathManager

# 临时添加路径到sys.path
with DynamicPathManager("./my_package") as manager:
    from my_module import some_function
    result = some_function()
    print(f"结果: {result}")

# 退出with块后，路径会自动从sys.path中移除
```

## 使用示例

### 基本用法

```python
from dynamic_path_manager import DynamicPathManager

with DynamicPathManager("./examples/a") as manager:
    from utils.helper import f
    f()  # 输出: a.utils.helper

with DynamicPathManager("./examples/b") as manager:
    from utils.helper import f
    f()  # 输出: b.utils.helper
```

### 高级用法

```python
from dynamic_path_manager import DynamicPathManager

# 如果你想保持模块在内存中，可以禁用缓存清理
with DynamicPathManager("./my_package", clear_cache=False) as manager:
    from my_module import expensive_function
    result = expensive_function()

# 检查路径是否在sys.path中
if manager.is_path_in_sys_path():
    print("路径当前在sys.path中")

# 获取管理的路径
print(f"管理的路径: {manager.get_path()}")
```

### 错误处理

```python
from dynamic_path_manager import DynamicPathManager

try:
    with DynamicPathManager("./nonexistent_path") as manager:
        from some_module import function
        function()
except ImportError as e:
    print(f"导入失败: {e}")
# 即使发生异常，路径仍会被清理
```

## API 参考

### DynamicPathManager

#### `__init__(package_path: str, clear_cache: bool = True)`

初始化动态路径管理器。

**参数:**

- `package_path` (str): 要添加到 sys.path 的路径
- `clear_cache` (bool): 退出时是否清除模块缓存（默认: True）

#### `__enter__() -> DynamicPathManager`

进入上下文管理器并将路径添加到 sys.path。

**返回值:**

- `DynamicPathManager`: 实例本身

#### `__exit__(exc_type, exc_val, exc_tb) -> None`

退出上下文管理器并进行清理。

**参数:**

- `exc_type`: 如果发生异常，异常类型
- `exc_val`: 如果发生异常，异常值
- `exc_tb`: 如果发生异常，异常追踪

#### `get_path() -> str`

获取被管理的绝对路径。

**返回值:**

- `str`: 绝对路径

#### `is_path_in_sys_path() -> bool`

检查被管理的路径是否当前在 sys.path 中。

**返回值:**

- `bool`: 如果路径在 sys.path 中返回 True，否则返回 False

## 使用场景

- **插件系统**: 从不同目录动态加载插件
- **测试**: 从各种位置导入测试模块
- **开发**: 在不同版本的模块之间切换
- **包管理**: 临时使用包的本地版本
- **微服务**: 从特定服务目录导入模块

## 贡献

欢迎贡献！请随时提交 Pull Request。对于重大更改，请先打开一个 issue 来讨论你想要更改的内容。

1. Fork 仓库
2. 创建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 开发

设置开发环境：

```bash
git clone https://github.com/yourusername/dynamic-path-manager.git
cd dynamic-path-manager
pip install -e ".[dev]"
```

运行测试：

```bash
pytest
```

运行代码检查：

```bash
flake8 src/
black src/
```

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 更新日志

### 1.0.0 (2024-01-XX)

- 初始版本
- 基本上下文管理器功能
- 模块缓存管理
- 全面的文档

## 致谢

- 灵感来源于 Python 项目中对干净动态导入的需求
- 感谢 Python 社区提供的优秀工具和文档
