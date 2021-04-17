#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION='''
module: count_page
author: PEDSF
description: Module that execute SQL request on database

options:
    db_name:
        description: the database name
        required: yes
    request:
        description: the request to apply
        required: yes
'''

EXAMPLES='''
- name: "SQL"
  count_page:
    db_name: "BDD"
    request: "select * from user;"

'''

RETURN='''
results:
    description: return the request result
'''


def main():
    module = AnsibleModule(
        argument_spec=dict(
            db_name=dict(required=True, type='str'),
            request=dict(required=True, type='str'),
        )
    )

    db_name_local = module.params.get('db_name')
    request_local = module.params.get('request')

    import MySQLdb

    db = MySQLdb.connect(db=db_name_local)
    cur = db.cursor()
    cur.execute(request_local)
    resultat_local = cur.fetchall()
    db.close

    module.exit_json(changed=False, results=resultat_local)

if __name__ == "__main__":
    main()
