### VinBigdata Interview

#### Hướng dẫn các bước chạy trực tiếp

Cd vào thư mục source code `InterviewTest`
```commandline
cd InterviewTest
```

Activate venv

```shell
./venv/Script/activate.bat
```

```commandline
pip install -r requirments.txt
```

Cài đặt và chạy MongoDB
```commandline
docker pull mongo:5.0.10
```
```commandline
docker run -d -p 27017:21017 mongo --port 27017 --bind_ip 0.0.0.0
```

Thêm vào file *hosts* dòng `127.0.0.1 mongodb` hoặc thêm thuộc tính `MONGO_URI = 'mongodb://127.0.0.1:27017/vinbigdata_interview'` vào `instance\config.py`

Tạo dữ liệu mẫu, dữ liệu này được import vào collection trong MongoDB
```commandline
flask --app flaskr init-db
```

Chạy dịch vụ API, các tùy chọn đặt trong dấu ngoặc vuông `[]` có thể bỏ đi cho gọn
```commandline
flask --app flaskr [--debug|--no-debug] run [--port 5000] [--host 0.0.0.0]
```

Hoặc chạy với Gunicorn
```commandline
gunicorn -w 4 --bind 0.0.0.0:5001 flaskr:create_app()
```

#### Test API theo yêu cầu của bài toán
- API ghi nhận cuộc gọi, ví dụ *username*=`cIeHdCeVPqipC`

```commandline
curl -i -H "Content-Type: application/json" -X PUT -d '{"call_duration": 1234567890}' http://localhost:5000/api/v1/mobile/cIeHdCeVPqipC/call
```
nếu thành công response trả về sẽ là thông tin chi tiết của cuộc gọi vừa được ghi nhận
```commandline
{
    "_id": "62eb04198b2e938a1af42248",
    "call_duration": 146413254,
    "username": "cIeHdCeVPqipC"
}
```

- API tính bill

```commandline
curl -i http://localhost:5000/api/v1/mobile/cIeHdCeVPqipC/billing
```
nếu thành công response có dạng 
```commandline
HTTP/1.1 200 OK
Server: Werkzeug/2.2.1 Python/3.10.5
Date: Wed, 03 Aug 2022 23:28:33 GMT
Content-Type: application/json
Content-Length: 47
Connection: close

{
  "block_count": 10726,
  "call_count": 93
}
```

#### Triển khai với Docker
```commandline
cd InterviewTest
```
```commandline
docker-compose up [-d]
```
Docker build thành công nhưng khi test API sẽ phát sinh lỗi 
```shell
{
    "error": "127.0.0.1:27017: [Errno 111] Connection refused, Timeout: 30s, Topology Description: <TopologyDescription id: 62eb08da4489d5c138e82f62, topology_type: Unknown, servers: [<ServerDescription ('127.0.0.1', 27017) server_type: Unknown, rtt: None, error=AutoReconnect('127.0.0.1:27017: [Errno 111] Connection refused')>]>"
}
```
Đây là lỗi cấu hình Docker
