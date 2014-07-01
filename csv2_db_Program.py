from ca.models import Program, University
import MySQLdb
import csv

db = MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        db = "test_caml"
        )

cur = db.cursor()
# Change encoding of all tables to utf8_general_ci
cur.execute('SHOW TABLES')
results=[]
for row in cur.fetchall(): results.append(row)
for row in results: cur.execute('ALTER TABLE %s CONVERT TO CHARACTER SET utf8 COLLATE     utf8_general_ci;' % (row[0]))
# Change the database charset
cur.execute("ALTER DATABASE test_caml CHARACTER SET utf8;")

def percentage_to_float(in_str):
    try:
        dummy = int(in_str[0])
        percentage_index = in_str.index('%')
        return (float(in_str[0:percentage_index]) / 100)
    except ValueError:
        return None
    except IndexError:
        return None

def dollar_to_float(in_str):
    if len(in_str) > 0:
        if in_str[0] == '$':
            in_str = in_str.replace(',','')
            return int(in_str[1:len(in_str)])
        else:
            return None
    else:
        return None

with open('Program Profile-Table 2.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
    next(spamreader, None) # Skip the header
    for row in spamreader:
        tmp = row[16]
        application_fee_tmp = float(tmp[1:len(tmp)])
        acceptance_rate_tmp = percentage_to_float(row[22])
        attendance_rate_tmp = percentage_to_float(row[23])
        percentage_international_tmp = percentage_to_float(row[25])
        percentage_chinese_tmp = percentage_to_float(row[26])
        tmp = row[27]
        try:
            dummy = int(tmp[0])
            average_gpa_tmp = float(tmp)
        except ValueError:
            average_gpa_tmp = None
        except IndexError:
            average_gpa_tmp = None

        tuition_tmp = dollar_to_float(row[30])
        books_supplies_tmp = dollar_to_float(row[31])
        living_cost_tmp = dollar_to_float(row[32])

        _, created = Program.objects.get_or_create(
                program_id = int(row[0]),
                program_category = row[1],
                university = row[2],
                name = row[3],
                degree = row[4],
                major = row[5],
                academic_professional = row[6],
                department = row[7],
                link = row[8],
                contact = row[9],
                description = row[10],
                length = row[11], 
                career = row[12],
                faculty = row[13],
                enrolling = row[14],
                application_deadline = row[15],
                application_fee = application_fee_tmp,
                application_material = row[17],
                required_tests = row[18],
                english_requirement = row[19],
                application_review = row[20],
                admission_decision = row[21],
                acceptance_rate = acceptance_rate_tmp,
                attendance_rate = attendance_rate_tmp,
                number_students = row[24],
                percentage_international = percentage_international_tmp,
                percentage_chinese = percentage_chinese_tmp,
                average_gpa = average_gpa_tmp,
                average_gre = row[28],
                undergrad_institution = row[29],
                tuition = tuition_tmp,
                books_supplies = books_supplies_tmp,
                living_cost = living_cost_tmp,
                scholarships_aid = row[33],
                )

        _, created = University.objects.get_or_create(
                name = row[2],
                year_founded = row[34],
                public_private = row[35],
                enrollment = row[36],
                location = row[37],
                setting = row[38],
                )

