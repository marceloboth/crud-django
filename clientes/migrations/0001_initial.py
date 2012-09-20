# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table('clientes_cliente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sobre_nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('data_nascimento', self.gf('django.db.models.fields.DateTimeField')()),
            ('profissao', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Profissao'])),
        ))
        db.send_create_signal('clientes', ['Cliente'])

        # Adding model 'Profissao'
        db.create_table('clientes_profissao', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('clientes', ['Profissao'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table('clientes_cliente')

        # Deleting model 'Profissao'
        db.delete_table('clientes_profissao')


    models = {
        'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'data_nascimento': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'profissao': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Profissao']"}),
            'sobre_nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clientes.profissao': {
            'Meta': {'object_name': 'Profissao'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['clientes']