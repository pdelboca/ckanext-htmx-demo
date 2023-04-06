import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from . import blueprint, helpers

class HtmxPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.ITemplateHelpers)
    

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "htmx")

    # IBlueprint

    def get_blueprint(self):
        return [blueprint.htmx]

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'add_param_or_remove_it_if_exist': helpers.add_param_or_remove_it_if_exist,
            'remove_param_if_exist': helpers.remove_param_if_exist,
        }
    
