{'name': 'Lateste Blog',
 'version': '16.0.1.0.0',
 'sequence': -1,
 'website': 'https://www.odoo.com/page/latest_blog',
 'category': 'Sales',
 'installable': True,
 'application': True,
 'auto_install': False,
 'depends': ['base', 'sale','website','web'],
 'data': [
      'views/snippet_inherit.xml',
      'views/new_snippet.xml'
 ],
 'assets':{
     'web.assets_frontend': [
         'latest_blog/static/src/js/latest_blog.js',
         'latest_blog/static/src/xml/latest_blog_template.xml',
         'latest_blog/static/src/css/latest_blog.scss'
     ]
     }
 }