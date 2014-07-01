# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'University.enrollment'
        db.alter_column(u'ca_university', 'enrollment', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    def backwards(self, orm):

        # Changing field 'University.enrollment'
        db.alter_column(u'ca_university', 'enrollment', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'ca.bs': {
            'Meta': {'object_name': 'BS'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bs_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'question_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.Question']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.calendar': {
            'Meta': {'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ca.lor': {
            'Meta': {'object_name': 'LOR'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'lor_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.package': {
            'Meta': {'object_name': 'Package'},
            'freq': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'package_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'package_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '19', 'decimal_places': '5', 'blank': 'True'})
        },
        u'ca.program': {
            'Meta': {'object_name': 'Program'},
            'academic_professional': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'acceptance_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '4', 'blank': 'True'}),
            'admission_decision': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'application_deadline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'application_fee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'application_material': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'application_review': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'attendance_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '4', 'blank': 'True'}),
            'average_gpa': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '4', 'blank': 'True'}),
            'average_gre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'books_supplies': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'career': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'english_requirement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enrolling': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'faculty': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'living_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'number_students': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'percentage_chinese': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '4', 'blank': 'True'}),
            'percentage_international': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '4', 'blank': 'True'}),
            'program_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'program_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'required_tests': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'scholarships_aid': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tuition': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'undergrad_institution': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'ca.ps': {
            'Meta': {'object_name': 'PS'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ps_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.question': {
            'Meta': {'object_name': 'Question'},
            'question': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'question_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'ca.resume': {
            'Meta': {'object_name': 'Resume'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resume_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.tracking': {
            'Meta': {'object_name': 'Tracking'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.Package']"}),
            'remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.university': {
            'Meta': {'object_name': 'University'},
            'enrollment': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'public_private': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'year_founded': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'ca.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'fav_program': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.Program']", 'symmetrical': 'False'}),
            'fav_university': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.University']", 'symmetrical': 'False'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.Package']", 'through': u"orm['ca.Tracking']", 'symmetrical': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'qq_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        }
    }

    complete_apps = ['ca']