# AWS Infrastructure Use Terraform
## Prerequisite
- AWS-CLI
- Credentials IAM User AWS
- Terraform

## Step 
- Siapkan IAM User AWS dengan policy 
    - EC2FullAccess
    - VPCFullAccess
    - S3FullAccess
- Buat Key Dan Simpan file csvnya
- Config AWS CLI dengan menggunakan command 
```
aws configure
```
- Input Key Dan Secret yang didapatkan dari file csv
- Install Terraform pada local machine anda
- Jalankan Command berikut agar bisa menjalankan code dari terraform
```
terraform init
```
- Jalankan Command berikut jika ingin melihat apa saja object yang nanti akan di create oleh terraform
```
terraform plan
```
- Jika ingin membuat infra nya jalankan command berikut
```
terraform apply
```
---
## Explanation
- file `main.tf`
    1. fungsi pertama adalah memilih provider yang akan mengimplementasikan terraform pada case ini kita akan menggunakan aws sehingga providernya `aws`
    2. `aws_vpc` adalah modul untuk membuat vpc dengan nama `main` yang didalam nya kita mendefinisikan segment IP
    3. `aws_subnet` adalah subnet dari vpc main yang kita buat pada langkah sebelumnya yang diconfig dengan salah satu ip yang kita jadikan subnet serta `map_public_ip_on_launch` yang bernilai true agar semua ec2 yang di creata pada subnet ini akan otomatis mendapatkan ip public
    4. `aws_internet_gateway` berfungsi untuk membuat vpc kita bisa berkomunikasi dengan internet
    5. `aws_route_table` berfungsi untuk routing traffic dari dan ke internet (public) pada blick `route` kita mendefinisikan ip segment internet dan `gateway_id` yang akan kita gunakan
    6. `aws_route_table_association` menghubungkan subnet dengan routing table yang telah kita buat 
    7. `aws_security_group` adalah firewall dari aws yang akan kita pasakan pada `vpc` yang telah kita buat, `ingress` adalah konfigurasi yang kita allow adalah port 22 dari public jadi kita bisa melakukan ssh ke ec2 yang menggunakan `vpc` dengan konfigurasi `security_group` ini 
    8. `aws_instance` adalah instace yang akan kita buat dengan mendefinisikan `ami` atau image os yang akan dipakai, spek dari server atau `instance_type`, `subnet` yang akan di gunakan serta `vpc_security_group_ids` yang digunakan, untuk `key_name` adalah credentials untuk akses awal ke server
    9. `aws_s3_bucket` adalah bucket atau object storage dari aws dengan nama `terraform-bucket` yang di config secara private
- file `output.tf`
File `output.tf` mempermudah kita melihat value setelah melakukan command ``terraform apply``

- file `variable.tf`
file untuk kita mendefinisikan variable yang nanti akan digunakan pada file `main.tf`

