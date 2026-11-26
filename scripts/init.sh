#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
VENV_DIR="${PROJECT_ROOT}/.venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
    echo "错误：找不到 Python 解释器：${PYTHON_BIN}" >&2
    exit 1
fi

SYSTEM_VERSION="$("${PYTHON_BIN}" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
VENV_VERSION=""

if [[ -x "${VENV_DIR}/bin/python" ]]; then
    VENV_VERSION="$("${VENV_DIR}/bin/python" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null || true)"
fi

if [[ -d "${VENV_DIR}" && "${VENV_VERSION}" != "${SYSTEM_VERSION}" ]]; then
    echo "检测到损坏或版本不匹配的虚拟环境，正在重建 ${VENV_DIR}"
    rm -rf "${VENV_DIR}"
fi

if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
    echo "使用 Python ${SYSTEM_VERSION} 创建虚拟环境"
    "${PYTHON_BIN}" -m venv "${VENV_DIR}"
fi

"${VENV_DIR}/bin/python" -m pip install --upgrade pip
"${VENV_DIR}/bin/python" -m pip install --upgrade -r "${PROJECT_ROOT}/requirements.txt"

echo
echo "环境初始化完成：${VENV_DIR}"
echo "激活命令：source \"${VENV_DIR}/bin/activate\""
