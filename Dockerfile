FROM python:3.13.4-slim AS builder

WORKDIR /social-stack

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

COPY . .
ENV PATH=/root/.local/bin:$PATH

RUN python render.py

FROM nginx:alpine

COPY --from=builder /social-stack/renders /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# FROM python:3.13.4-slim
#
# WORKDIR /social-stack
# COPY --from=builder /social-stack/renders ./renders
#
# EXPOSE 89
#
# CMD ["python", "-m", "http.server", "80", "--directory", "renders"]
# CMD [ "python", "./render.py" ]
