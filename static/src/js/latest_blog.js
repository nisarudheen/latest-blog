odoo.define('latest_blog.blog', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core =  require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
           var self = this;
           rpc.query({
               route: '/latest_blog',
               params: {},
           }).then(function (result) {
           console.log(result)
           var name = result;
           $('.qweb_latest_blog').append(Qweb.render('latest_blog.blog_snippet',{name}));
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});