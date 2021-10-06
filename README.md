<div align="center">
  <center>
    <img width="400" height="" src='https://svgshare.com/i/at2.svg' title='' />
  </center>
</div>
<div align="center">
  <center>
    <h1 style="margin-top:10px;" align="center"> 🚀
      <strong> Easy Parking </strong> 🔭
    </h1>
  </center>
</div>

## 🐧 Project explanation

The application aims to make it easier for users to find a parking space quickly and efficiently, being able to reserve at the same time that the car park owners offer their spaces with the option of adding other extra services such as laundry or workshop, based on existing applications to investigate their strengths and correct their flaws to create friendly and profitable software for all parties involved, having flexibility in its use

## 🐟 To get started 

1. Clone this repository: `https://gitlab.com/fabianvera728/easy-parking.git`.

### 👾 Configure the database

1. Create a database in PostgreSQL: `create database easy_parking;`.
2. Create a user admin: `create user admin_parking with encrypted password 'admin123';`.
3. Set privileges to user admin: `grant all privileges on database easy_parking to admin_parking;`.

### 🐋 Configure and run the django project

1. Create a virtual environment in `/backend/easy_parking/`: `python3 -m venv venv`. Being "venv" the name for virtual environment.
2. Access to virtual environment: `source venv/bin/activate`.
3. Install packages requires: `pip3 install -r requirements.txt`.
4. Make migrations for Django project. In folder `/backend/easy_parking/` execute `python3 manage.py makemigrations`.
5. Migrate to database: `python3 manage.py migrate`.
6. Run: `python3 manage.py runserver`.

### 🐋 Configure and run the ionic project

1. C2 : ``.

## 📷 Screenshots
### 🦀 Home

## 🖋️ Authors

The developers have contributed to this project:

* Wilmer Rodríguez Sánchez - <a href="https://gitlab.com/WilmerRS10"> WilmerRS10 </a>
* Fabian Vera Carrillo - <a href="https://gitlab.com/fabianvera728"> fabianvera728 </a>
