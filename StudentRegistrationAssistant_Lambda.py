{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import json\
\
\
# Mock data for demonstration purposes\
uiucmcs_data = \{\
        1: \{"courseName": "CS 598", "courseTitle": "Advanced Bayesian Modeling", "Reviews": 6, "Difficulty(1-5)": 4.3, "Workload(hrs/wk)": 19.5, "Rating(1-5)": 4.5, "Semester": "spring"\},\
        2: \{"courseName": "CS 525", "courseTitle": "Advanced Distributed Systems", "Reviews": 6, "Difficulty(1-5)": 5, "Workload(hrs/wk)": 16, "Rating(1-5)": 4.5, "Semester": "spring"\},\
        3: \{"courseName": "CS 441", "courseTitle": "Machine Learning", "Reviews": 31, "Difficulty(1-5)": 2.6, "Workload(hrs/wk)": 12.5, "Rating(1-5)": 2.6, "Semester": "fall"\},\
        4: \{"courseName": "CS 498", "courseTitle": "Cloud Computing Applications", "Reviews": 27, "Difficulty(1-5)": 4.3, "Workload(hrs/wk)": 110, "Rating(1-5)": 4.6, "Semester": "spring"\},\
        5: \{"courseName": "CS 435", "courseTitle": "Cloud Networking", "Reviews": 10, "Difficulty(1-5)": 4.6, "Workload(hrs/wk)": 19.5, "Rating(1-5)": 4.8, "Semester": "spring"\},\
    	6: \{"courseName": "CS 445", "courseTitle": "Computational Photography", "Reviews": 8, "Difficulty(1-5)": 3.9, "Workload(hrs/wk)": 17.5, "Rating(1-5)": 4.8, "Semester": "spring"\},\
    	7: \{"courseName": "CS 411", "courseTitle": "Database Systems", "Reviews": 12, "Difficulty(1-5)": 3.1, "Workload(hrs/wk)": 10, "Rating(1-5)": 4.3, "Semester": "fall"\},\
    	8: \{"courseName": "CS 437", "courseTitle": "Internet of Things", "Reviews": 15, "Difficulty(1-5)": 3.8, "Workload(hrs/wk)": 11, "Rating(1-5)": 4.3, "Semester": "summer"\},\
    	9: \{"courseName": "CS 447", "courseTitle": "Natural Language Processing", "Reviews": 9, "Difficulty(1-5)": 3.6, "Workload(hrs/wk)": 16.5, "Rating(1-5)": 4.5, "Semester": "fall"\},\
    \}  \
\
\
\
def get_named_parameter(event, name):\
    return next(item for item in event['parameters'] if item['name'] == name)['value']\
\
def get_named_property(event, name):\
    return next(item for item in event['requestBody']['content']['application/json']['properties'] if item['name'] == name)['value']\
\
def coursesStats(event):\
    courseName = get_named_parameter(event, 'course')\
    semester = get_named_parameter(event, 'semester')\
    \
    print ("courseName:", courseName)\
    print ("semester:", semester)\
    \
    # TODO: implement logic\
    \
    # Search for the couse data in the dictionary\
 \
    for id, course_info in uiucmcs_data.items():\
            print ("id:", id)\
            print ("course_info:", course_info)\
            if course_info['courseName'].lower() == courseName.lower():\
                print ("****** Found the right couse:", course_info)\
                return course_info\
            # else:\
            #     print ("****** Did not find the right couse")\
            #     return \{\
            #         "requestStatus":"This course is not offered at this moment. Please follow up with the office of the Registar at https://registrar.illinois.edu/registration/"\
            #     \}\
                \
    \
    \
    # return [\
    #   \{\
    #     "courseName": "CS101", \
    #     "numberOfStudents": 100,\
    #     "averageGrade": 90\
    #   \},\
    #   \{  \
    #     "courseName": "MATH201",\
    #     "numberOfStudents": 80,\
    #     "averageGrade": 82  \
    #   \}\
    # ]\
\
def registerClass(event):\
    courseName = get_named_parameter(event, 'course')\
    semester = get_named_parameter(event, 'semester')\
    \
    # TODO: implement course registration logic\
\
    return \{\
      "registrationStatus": "Registered successfully. A notificatio was sent to your studen email with  for registrationd details for " + courseName \
    \}\
    \
    \
    \
  \
def lambda_handler(event, context):\
\
    print(event)\
\
    response_code = 200\
    action_group = event['actionGroup']\
    api_path = event['apiPath']\
    \
    if api_path == '/coursesStats':\
        result = coursesStats(event)\
    elif api_path == '/registerClass':\
        result = registerClass(event) \
    else:\
        response_code = 404\
        result = f"Unrecognized api path: \{action_group\}::\{api_path\}"\
        \
    response_body = \{\
        'application/json': \{\
            'body': result\
        \}\
    \}\
        \
    action_response = \{\
        'actionGroup': event['actionGroup'],\
        'apiPath': event['apiPath'],\
        'httpMethod': event['httpMethod'],\
        'httpStatusCode': response_code,\
        'responseBody': response_body\
    \}\
\
    api_response = \{'messageVersion': '1.0', 'response': action_response\}\
    return api_response}