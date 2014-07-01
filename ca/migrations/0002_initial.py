# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'ca_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'ca', ['Question'])

        # Adding model 'Package'
        db.create_table(u'ca_package', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=19, decimal_places=5, blank=True)),
            ('freq', self.gf('django.db.models.fields.CharField')(max_length=31, blank=True)),
        ))
        db.send_create_signal(u'ca', ['Package'])

        # Adding model 'University'
        db.create_table(u'ca_university', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year_founded', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('public_private', self.gf('django.db.models.fields.CharField')(max_length=31, blank=True)),
            ('enrollment', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'ca', ['University'])

        # Adding model 'Program'
        db.create_table(u'ca_program', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program_category', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('university', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('academic_professional', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('link', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('contact', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('length', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('career', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('faculty', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('enrolling', self.gf('django.db.models.fields.CharField')(max_length=31, blank=True)),
            ('application_deadline', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('application_fee', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('application_material', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('required_tests', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('english_requirement', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('application_review', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('admission_decision', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('acceptance_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=4, blank=True)),
            ('attendance_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=4, blank=True)),
            ('number_students', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('percentage_international', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=4, blank=True)),
            ('percentage_chinese', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=4, blank=True)),
            ('average_gpa', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=4, blank=True)),
            ('average_gre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('undergrad_institution', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('tuition', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('books_supplies', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('living_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('scholarships_aid', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'ca', ['Program'])

        # Adding model 'User'
        db.create_table(u'ca_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=31, null=True, blank=True)),
            ('skype_id', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('qq_id', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
        ))
        db.send_create_signal(u'ca', ['User'])

        # Adding M2M table for field fav_program on 'User'
        m2m_table_name = db.shorten_name(u'ca_user_fav_program')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'ca.user'], null=False)),
            ('program', models.ForeignKey(orm[u'ca.program'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'program_id'])

        # Adding M2M table for field fav_university on 'User'
        m2m_table_name = db.shorten_name(u'ca_user_fav_university')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'ca.user'], null=False)),
            ('university', models.ForeignKey(orm[u'ca.university'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'university_id'])

        # Adding model 'Resume'
        db.create_table(u'ca_resume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ca', ['Resume'])

        # Adding model 'PS'
        db.create_table(u'ca_ps', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User'])),
            ('title', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ca', ['PS'])

        # Adding model 'LOR'
        db.create_table(u'ca_lor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ca', ['LOR'])

        # Adding model 'BS'
        db.create_table(u'ca_bs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.Question'])),
            ('user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User'])),
            ('answer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'ca', ['BS'])

        # Adding model 'Tracking'
        db.create_table(u'ca_tracking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.Package'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User'])),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('remaining', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=31, blank=True)),
        ))
        db.send_create_signal(u'ca', ['Tracking'])

        # Adding model 'Calendar'
        db.create_table(u'ca_calendar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ca', ['Calendar'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'ca_question')

        # Deleting model 'Package'
        db.delete_table(u'ca_package')

        # Deleting model 'University'
        db.delete_table(u'ca_university')

        # Deleting model 'Program'
        db.delete_table(u'ca_program')

        # Deleting model 'User'
        db.delete_table(u'ca_user')

        # Removing M2M table for field fav_program on 'User'
        db.delete_table(db.shorten_name(u'ca_user_fav_program'))

        # Removing M2M table for field fav_university on 'User'
        db.delete_table(db.shorten_name(u'ca_user_fav_university'))

        # Deleting model 'Resume'
        db.delete_table(u'ca_resume')

        # Deleting model 'PS'
        db.delete_table(u'ca_ps')

        # Deleting model 'LOR'
        db.delete_table(u'ca_lor')

        # Deleting model 'BS'
        db.delete_table(u'ca_bs')

        # Deleting model 'Tracking'
        db.delete_table(u'ca_tracking')

        # Deleting model 'Calendar'
        db.delete_table(u'ca_calendar')


    models = {
        u'ca.bs': {
            'Meta': {'object_name': 'BS'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.package': {
            'Meta': {'object_name': 'Package'},
            'freq': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'link': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'living_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'number_students': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'percentage_chinese': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '4', 'blank': 'True'}),
            'percentage_international': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '4', 'blank': 'True'}),
            'program_category': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'required_tests': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'scholarships_aid': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'tuition': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'undergrad_institution': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'ca.ps': {
            'Meta': {'object_name': 'PS'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.User']"})
        },
        u'ca.question': {
            'Meta': {'object_name': 'Question'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'ca.resume': {
            'Meta': {'object_name': 'Resume'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.Package']", 'through': u"orm['ca.Tracking']", 'symmetrical': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'qq_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        }
    }

    complete_apps = ['ca']