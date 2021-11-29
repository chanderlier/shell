resource "alicloud_oss_bucket" "bucket-acl" {
  bucket = var.oss_bucket_name
  acl    = "private"
}
resource "alicloud_ram_user" "user" {
  name         = var.ram_user_name          # 用户名
  comments     = "oss test"
  force        = true
}
resource "alicloud_ram_access_key" "ak" {
  user_name   = alicloud_ram_user.user.name
  secret_file = "accesskey.txt"                # 保存AccessKey的文件名
}
resource "alicloud_ram_policy" "policy" {
  policy_name     = var.ram_policy_name
  policy_document = <<EOF
  {
    "Statement": [
      {
        "Action": [
          "oss:ListObjects",
          "oss:GetObject"
        ],
        "Effect": "Allow",
        "Resource": [
          "acs:oss:*:*:var.oss_bucket_name",
          "acs:oss:*:*:var.oss_bucket_name/*"
        ]
      }
    ],
      "Version": "1"
  }
  EOF
  description = "this is a policy test"
  force = true
}
# 将ram.user和policy绑定
resource "alicloud_ram_user_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  user_name   = alicloud_ram_user.user.name
}

resource "alicloud_ram_role" "role" {
  name = var.ram_role_name
  document    = <<EOF
  {
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
          "RAM": [
            "${var.ARN}"
          ]
        }
      }
    ],
    "Version": "1"
  }
  EOF
  description = "this is a role test."
  force       = true
}
# 将ram.role与policy绑定
resource "alicloud_ram_role_policy_attachment" "attach" {
  policy_name = alicloud_ram_policy.policy.policy_name
  policy_type = alicloud_ram_policy.policy.type
  role_name   = alicloud_ram_role.role.name
}