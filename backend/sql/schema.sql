
CREATE TABLE classes(
  classname VARCHAR(40) NOT NULL,
  department VARCHAR(10) NOT NULL,
  title VARCHAR(100) NOT NULL,
  classnumber INTEGER NOT NULL,
  credits INTEGER,
  workload INTEGER,
  PRIMARY KEY(classname)
);