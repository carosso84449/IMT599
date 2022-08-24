/****** Object:  Table [dbo].[small_spoiled]    Script Date: 8/23/2022 9:53:23 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[small_spoiled](
	[ballot_id] [nvarchar](max) NULL,
	[contest_data] [nvarchar](max) NULL,
	[selection_id] [nvarchar](max) NULL,
	[tally] [nchar](10) NULL,
	[ledger_start_transaction_id] [bigint] GENERATED ALWAYS AS transaction_id START HIDDEN NOT NULL,
	[ledger_end_transaction_id] [bigint] GENERATED ALWAYS AS transaction_id END HIDDEN NULL,
	[ledger_start_sequence_number] [bigint] GENERATED ALWAYS AS sequence_number START HIDDEN NOT NULL,
	[ledger_end_sequence_number] [bigint] GENERATED ALWAYS AS sequence_number END HIDDEN NULL,
	[contest_id] [nvarchar](max) NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
WITH
(
LEDGER = ON (LEDGER_VIEW = small_spoiled_Ledger)
)
GO


