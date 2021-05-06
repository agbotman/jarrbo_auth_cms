from menus.base import NavigationNode, Modifier
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Add a navigation node to the end of the existing menu
@menu_pool.register_modifier
class AuthModifier(Modifier):
	def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
		if not post_cut:
			if request.user.is_authenticated:
				menuname = _("Profile")
			else:
				menuname = _("Login")
			nodes.append(NavigationNode(menuname, reverse("jarrbo_auth:profile"), 1))
		return nodes