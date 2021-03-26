import streamlit as st
from settings import *
from database import connection

define(st)
options(st, connection)
