--These SQL queries were run on the stack exchange data explorer : http://data.stackexchange.com/stackoverflow/queries--
-- All our queries are on : http://data.stackexchange.com/users/13676/rishi-josan


-- Get list of prospective answerers for a set of 3 Tags : Before a certain Post's CreationDate  :http://data.stackexchange.com/stackoverflow/query/188064/get-list-of-prospective-answerers-for-a-set-of-3-tags-before-a-certain-posts-c
Select ParentID, Id, OwnerUserId FROM Posts WHERE ParentId IN (Select PostId From PostTags where TagId = '5990' INTERSECT
Select PostId From PostTags where TagId = '16'  INTERSECT Select PostId From PostTags where TagId = '12408') AND CreationDate < (Select CreationDate FROM Posts WHERE Id = '9299346') Order By ParentId ASC

-- Get list of prospective answerers (From Comments) for a set of 3 Tags : http://data.stackexchange.com/stackoverflow/query/188045/get-list-of-prospective-answerers-from-comments-for-a-set-of-3-tags
Select PostId, Id, UserId FROM Comments WHERE PostId IN (Select PostId From PostTags where TagId = '5990' INTERSECT
Select PostId From PostTags where TagId = '16'  INTERSECT Select PostId From PostTags where TagId = '12408') Order By PostId ASC

-- Get list of prospective answerers for a set of 3 Tags : http://data.stackexchange.com/stackoverflow/query/188038/get-list-of-prospective-answerers-for-a-set-of-3-tags
Select ParentID, Id, OwnerUserId FROM Posts WHERE ParentId IN (Select PostId From PostTags where TagId = '5990' INTERSECT
Select PostId From PostTags where TagId = '16'  INTERSECT Select PostId From PostTags where TagId = '12408') Order By ParentId ASC

-- Get Count of tags for user : http://data.stackexchange.com/stackoverflow/query/187918/get-count-of-tags-for-user
Select TagId, Count(TagId) FROM PostTags WHERE PostId IN (Select Id From Posts Where OwnerUserId = '1170240') Group By TagId Order By Count(TagId) DESC

