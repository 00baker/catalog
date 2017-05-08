from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import *
from setup import Base, Category, CategoryItem
from sqlalchemy.orm import sessionmaker

"""Used for seeding the database for testing and dev purposes"""
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

## Clear the tables
session.query(Category).delete()
session.query(CategoryItem).delete()

## Add categories
sample_categories = ['Music', 'Video', '3D']

for category_name in sample_categories:
    category = Category(category_name)
    session.add(category)
session.commit()

## Add items
sample_items = {'Eminem': 1, 'Funny Cat': 2, 'Anime': 3}

for item_title, item_category in sample_items.iteritems():
    item = CategoryItem(item_title, "Sample description", item_category)
    session.add(item)
session.commit()
