var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
// config path
app.use('', express.static(path.join(__dirname, 'public/views')));
app.use('/css', express.static(path.join(__dirname,'public/css')))
app.use('/js', express.static(path.join(__dirname,'public/js')))
app.use('/plugins', express.static(path.join(__dirname,'public/plugins')))
app.use('/assets', express.static(path.join(__dirname,'public/assets')))

app.use('/', indexRouter);
app.use('/users', usersRouter);

module.exports = app;
