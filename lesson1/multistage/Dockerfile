# stage 1
FROM golang:1.17 AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server

# stage 2
FROM alpine:latest
WORKDIR /root
COPY --from=builder /app/server .
EXPOSE 8080
CMD ["./server"]