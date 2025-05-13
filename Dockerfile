FROM python:3.9-slim

WORKDIR /app

# 安装应用依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 安装OpenTelemetry自动检测工具
RUN pip install --no-cache-dir \
    opentelemetry-distro \
    opentelemetry-exporter-otlp \
    opentelemetry-instrumentation-flask \
    opentelemetry-instrumentation-requests

# 安装所有自动instrumentation
RUN opentelemetry-bootstrap -a install

# 复制应用代码
COPY main.py .

# 设置环境变量用于无侵入式追踪
ENV PYTHONPATH="/app:${PYTHONPATH}"

# 启动命令（使用opentelemetry-instrument包装器来实现无侵入式追踪）
CMD ["opentelemetry-instrument", "python", "main.py"]
