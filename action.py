# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template

class Action(object):
    """docstring for Action"""
    def __init__(self, node):
        self.node = node

class View(Action):
    """docstring for View"""
    def apply(self):
    	try:
        	text = unicode(open(os.path.join(self.node.root, self.node.path)).read())
        except UnicodeDecodeError:
        	return None
        context = { 'text' : text }
        return context