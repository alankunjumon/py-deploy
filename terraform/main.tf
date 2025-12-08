terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  required_version = ">=1.2.0"

  backend "s3" {
    bucket         = "py-deploy-state-alankunjumon-2025"
    key            = "global/s3/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "py-deploy-lock-table"
    encrypt        = true
  }
}
provider "aws"{
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0ecb62995f68bb549"
  instance_type = "t2.micro"

  key_name = "py-deploy-key"

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  tags = {
    Name = "Terraform-py-deploy"
  }
}

resource "aws_security_group" "web_sg" {
  name        = "py-deploy-sg-terraform"
  description = "Allow SSH and HTTP"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress{
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "server_public_ip" {
  description = "The public ip address of the server"
  value       = aws_instance.app_server.public_ip
}
