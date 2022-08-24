DECLARE @ContainerTable TABLE(
	[ballot_id] NVARCHAR(MAX),
    [json_start] NVARCHAR(MAX)
);

INSERT INTO @ContainerTable([ballot_id], [json_start])
SELECT [ballot_id], JSON_query(contest_data, '$') as json_start
FROM [small_spoiled];

DECLARE @ContainerTable1 TABLE(
	[ballot_id] NVARCHAR(MAX),
    [contest_id] NVARCHAR(MAX),
    [Value] NVARCHAR(MAX)
);

INSERT INTO @ContainerTable1([ballot_id], [contest_id], [Value])
SELECT [ballot_id], [key], [value] 
FROM @ContainerTable AS x
CROSS APPLY OPENJSON(x.json_start, '$');

DECLARE @ContainerTable1_5 TABLE(
	[ballot_id] NVARCHAR(MAX),
    [contest_id] NVARCHAR(MAX),
    [Value] NVARCHAR(MAX)
);

INSERT INTO @ContainerTable1_5([ballot_id], [contest_id], [Value])
SELECT * FROM @ContainerTable1

DECLARE @ContainerTable2 TABLE(
	[ballot_id] NVARCHAR(MAX),
	[contest_id] NVARCHAR(MAX),
    [json2] NVARCHAR(MAX)
);

INSERT INTO @ContainerTable2([ballot_id], [contest_id], [json2])
SELECT ballot_id, contest_id, JSON_query([Value], '$.selections')
FROM @ContainerTable1_5;

DECLARE @ContainerTable3 TABLE(
	[ballot_id] NVARCHAR(MAX),
	[contest_id] NVARCHAR(MAX),
    [selection_id] NVARCHAR(MAX),
    [json3] NVARCHAR(MAX)
);

INSERT INTO @ContainerTable3([ballot_id], [contest_id], [selection_id], [json3])
SELECT [ballot_id], [contest_id], [key], [value]
FROM @ContainerTable2 AS T2
CROSS APPLY OPENJSON(T2.[json2]);

DECLARE @ContainerTable4 TABLE(
	[ballot_id] NVARCHAR(MAX),
	[contest_id] NVARCHAR(MAX),
    [selection_id] NVARCHAR(MAX),
    [tally] NVARCHAR(MAX)
);

INSERT INTO @ContainerTable4([ballot_id], [contest_id], [selection_id], [tally])
SELECT [ballot_id], [contest_id], [selection_id], JSON_value([json3], '$.tally')
FROM @ContainerTable3;

INSERT INTO [dbo].[small_spoiled_final]
SELECT * FROM @ContainerTable4