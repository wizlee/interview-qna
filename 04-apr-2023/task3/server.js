'use strict';

const express = require('express');
const app = express();
app.use(express.json());

// Just for documentation. In a real DB, below will be the data type used taking into consideration 2-byte long Unicode characters
// id: nvarchar (200)
// name: nvarchar (200)
const db = {}

app.post('/candidates', function (req, res) {
  if (!req.is('application/json') || isEmtpy(req.body)) {
    res.sendStatus(400);
    return;
  }

  let candidate = req.body;
  db[candidate.id] = candidate;

  res.sendStatus(200).end();
});

app.get('/candidates/search', function (req, res) {
  if (!req.query?.skills) {
    res.sendStatus(400);
    return;
  }

  let querySkills = req.query.skills.split(',');
  let bestMatch = null;
  let maxSkills = 0;

  for (let id in db) {
    let candidate = db[id];
    let skillCount = 0;
    for (let i = 0; i < candidate.skills.length; i++) {
      if (querySkills.includes(candidate.skills[i])) {
        skillCount++;
      }
    }
    if (skillCount > maxSkills) {
      bestMatch = candidate;
      maxSkills = skillCount;
    }
  }

  if (bestMatch) {
    res.contentType("application/json");
    res.json(bestMatch);
  } else {
    res.sendStatus(404);
  }
});

function isEmtpy(obj) {
  return obj.constructor === Object && Object.keys(obj).length === 0;
}

app.listen(process.env.HTTP_PORT || 3000);
