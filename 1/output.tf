output "instance_id" {
  value = aws_instance.ubuntu.id
}

output "public_ip" {
  value = aws_instance.ubuntu.public_ip
}

output "bucket_arn" {
  value = aws_s3_bucket.b.arn
}
