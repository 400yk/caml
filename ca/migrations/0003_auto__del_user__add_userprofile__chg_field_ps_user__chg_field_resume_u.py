# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'ca_user')

        # Removing M2M table for field fav_program on 'User'
        db.delete_table(db.shorten_name(u'ca_user_fav_program'))

        # Removing M2M table for field fav_university on 'User'
        db.delete_table(db.shorten_name(u'ca_user_fav_university'))

        # Adding model 'UserProfile'
        db.create_table(u'ca_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=31, null=True, blank=True)),
            ('skype_id', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('qq_id', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ca', ['UserProfile'])

        # Adding M2M table for field fav_program on 'UserProfile'
        m2m_table_name = db.shorten_name(u'ca_userprofile_fav_program')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'ca.userprofile'], null=False)),
            ('program', models.ForeignKey(orm[u'ca.program'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'program_id'])

        # Adding M2M table for field fav_university on 'UserProfile'
        m2m_table_name = db.shorten_name(u'ca_userprofile_fav_university')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm[u'ca.userprofile'], null=False)),
            ('university', models.ForeignKey(orm[u'ca.university'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'university_id'])


        # Changing field 'PS.user'
        db.alter_column(u'ca_ps', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.UserProfile']))

        # Changing field 'Resume.user'
        db.alter_column(u'ca_resume', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.UserProfile']))

        # Changing field 'BS.user_id'
        db.alter_column(u'ca_bs', 'user_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.UserProfile']))

        # Changing field 'LOR.user'
        db.alter_column(u'ca_lor', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.UserProfile']))

        # Changing field 'Tracking.user'
        db.alter_column(u'ca_tracking', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.UserProfile']))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'ca_user', (
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=31, null=True, blank=True)),
            ('skype_id', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=63)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('qq_id', self.gf('django.db.models.fields.CharField')(max_length=63, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=63)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
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

        # Deleting model 'UserProfile'
        db.delete_table(u'ca_userprofile')

        # Removing M2M table for field fav_program on 'UserProfile'
        db.delete_table(db.shorten_name(u'ca_userprofile_fav_program'))

        # Removing M2M table for field fav_university on 'UserProfile'
        db.delete_table(db.shorten_name(u'ca_userprofile_fav_university'))


        # Changing field 'PS.user'
        db.alter_column(u'ca_ps', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User']))

        # Changing field 'Resume.user'
        db.alter_column(u'ca_resume', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User']))

        # Changing field 'BS.user_id'
        db.alter_column(u'ca_bs', 'user_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User']))

        # Changing field 'LOR.user'
        db.alter_column(u'ca_lor', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User']))

        # Changing field 'Tracking.user'
        db.alter_column(u'ca_tracking', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ca.User']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'ca.bs': {
            'Meta': {'object_name': 'BS'},
            'answer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.Question']"}),
            'user_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.UserProfile']"})
        },
        u'ca.calendar': {
            'Meta': {'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ca.lor': {
            'Meta': {'object_name': 'LOR'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.UserProfile']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.UserProfile']"})
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.UserProfile']"})
        },
        u'ca.tracking': {
            'Meta': {'object_name': 'Tracking'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.Package']"}),
            'remaining': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '31', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ca.UserProfile']"})
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
        u'ca.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'fav_program': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.Program']", 'symmetrical': 'False'}),
            'fav_university': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.University']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'packages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ca.Package']", 'through': u"orm['ca.Tracking']", 'symmetrical': 'False'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '31', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'qq_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'skype_id': ('django.db.models.fields.CharField', [], {'max_length': '63', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ca']