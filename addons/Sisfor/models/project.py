# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'
    
    # Tambahan field untuk project di PT Laudza
    start_date = fields.Date(string='Tanggal Mulai')
    end_date = fields.Date(string='Tanggal Selesai')
    description = fields.Text(string='Deskripsi')
    progress = fields.Float(string='Progress (%)', compute='_compute_progress')
    
    @api.depends('task_ids.stage_id')
    def _compute_progress(self):
        for project in self:
            total_tasks = len(project.task_ids)
            if total_tasks:
                completed_tasks = len(project.task_ids.filtered(lambda task: task.stage_id.fold))
                project.progress = (completed_tasks / total_tasks) * 100
            else:
                project.progress = 0.0

class ProjectItem(models.Model):
    _name = 'laudza.project.item'
    _description = 'Item Pekerjaan Proyek'
    
    name = fields.Char(string='Nama Item', required=True)
    project_id = fields.Many2one('project.project', string='Proyek', required=True)
    description = fields.Text(string='Deskripsi')
    date_input = fields.Date(string='Tanggal Input', default=fields.Date.context_today)
    
class ProjectDocumentation(models.Model):
    _name = 'laudza.project.documentation'
    _description = 'Dokumentasi Proyek'
    
    name = fields.Char(string='Nama File', required=True)
    project_id = fields.Many2one('project.project', string='Proyek', required=True)
    file = fields.Binary(string='File Dokumentasi', attachment=True)
    date_upload = fields.Date(string='Tanggal Upload', default=fields.Date.context_today)
    description = fields.Text(string='Deskripsi')
    
class ProjectKendala(models.Model):
    _name = 'laudza.project.kendala'
    _description = 'Kendala Proyek'
    
    name = fields.Char(string='Nama Kendala', required=True)
    project_id = fields.Many2one('project.project', string='Proyek', required=True)
    kendala_date = fields.Date(string='Tanggal Kendala', default=fields.Date.context_today)
    description = fields.Text(string='Deskripsi Kendala', required=True)
    severity = fields.Selection([
        ('low', 'Rendah'),
        ('medium', 'Sedang'),
        ('high', 'Tinggi'),
        ('critical', 'Kritis')
    ], string='Tingkat Keparahan', default='medium')
    state = fields.Selection([
        ('open', 'Terbuka'),
        ('in_progress', 'Dalam Penanganan'),
        ('resolved', 'Selesai')
    ], string='Status', default='open')
    feedback_ids = fields.One2many('laudza.project.feedback', 'constraint_id', string='Masukan/Arahan')
    
class ProjectFeedback(models.Model):
    _name = 'laudza.project.feedback'
    _description = 'Masukan/Arahan Proyek'
    
    constraint_id = fields.Many2one('laudza.project.constraint', string='Kendala', required=True)
    user_id = fields.Many2one('res.users', string='Pemberi Masukan', default=lambda self: self.env.user, required=True)
    date_feedback = fields.Date(string='Tanggal Masukan', default=fields.Date.context_today)
    content = fields.Text(string='Isi Masukan', required=True)