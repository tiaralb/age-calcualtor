from flask import Flask, jsonify, request
import datetime


app = Flask(__name__)


def get_age(birthdate,birthmonth,birthyear):
    currentDay = datetime.datetime.now().day
    currentMonth = datetime.datetime.now().month
    currentYear = datetime.datetime.now().year
    
    
    # date(year, month, day)
    birth_date = datetime.date(birthyear, birthmonth, birthdate)
    
    end_date = datetime.date(currentYear, currentMonth, currentDay)
    
    time_difference = end_date - birth_date
    
    age_in_days = int(time_difference.days)
    age_in_year = currentYear-birthyear
    
    left_in_days=age_in_days%365
    
    
    return age_in_year,left_in_days



@app.route('/api/age', methods=['GET'])
def main():
    try:
        name = request.json['name']
        date = request.json['date']
        month = request.json['month']
        year = request.json['year']
        
        age=get_age(date,month,year)
        
        msg=f'hallo {name}, umurmu {age[0]} tahun, {age[1]} hari'
    except:
        msg='error'
        
        
        
    
    return jsonify({'msg':msg})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

