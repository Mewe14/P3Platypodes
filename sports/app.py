import os
from flask import Flask, Blueprint, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc