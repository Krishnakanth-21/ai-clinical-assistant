resource "aws_s3_bucket" "raw_data" {
  bucket = "${var.project_name}-${var.environment}-raw-data"

  tags = {
    Name        = "${var.project_name}-raw-data"
    Environment = var.environment
    Project     = var.project_name
  }
}
