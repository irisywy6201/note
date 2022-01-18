- https://github.com/metabase/metabase/issues/12650
- https://cljdoc.org/d/metabase-core/metabase-core/1.0.0-SNAPSHOT/api/metabase.query-processor.middleware.cache
- https://github.com/metabase/metabase/issues/10745
- https://kapwi.ng/c/C8i2CkSpiO
- https://segmentfault.com/q/1010000010636309
- https://stackoverflow.com/questions/53516594/why-do-i-keep-getting-delete-cr-prettier-prettier
- SQLAlchemy             1.3.24
SQLAlchemy-Utils       0.37.8
- https://rockset.com/blog/handling-slow-queries-in-mongodb-part-2-solutions/
- mongosqld --config example-mongosqld-config.yml


Why?
那首先會先介紹為甚麼會需要使用replicaSet，在過往來有沒這種架構時的mongodb就是像這樣單顆mongo裝在某一台server，這時你的application不管是讀或寫都是對這棵mongo去做操作，那這時就會有一個問題，就是當可能遇到突發狀況時，比如說這顆mongo故障了….那這時在你修好的這段時間，application就暫時連不到資料庫，那使用者就可能就會抱怨呀，或是當這顆mongo需要做版本升級時也會很難做到讓使用者無感的升級，所以replicaset就是為了解決這種問題所衍生的一種架構

What?
那replicaset是甚麼呢? 他主要就是一種用來解決上述單顆mongo所造成的問題的一種高可用性叢集架構，那高可用簡單來說，就是一種讓服務（幾乎）永遠不會下線的能力，那要達到高可用其實就是把資料備份在各地，這樣當某個壞了還有其他備份資料可以用，所以在這個架構中會有多顆mongo，然後每個mongo都會有不同的角色，主要分為primary跟secondary，只會有一個人是primary，其他人都是secondary，可以把他想成primary是主，secondary是從，所以說在這個架構中資料只會從primary寫入，然後secondary會一直同步的primary的最新資料，所以就有點像是你把資料備份到三個mongo裡面，那他的好處就是，當primary故障時還有其他的節點可以連，資料也都還在，因此他就是有所謂的資料的容災和備份作用
是最常見使用情境是三顆，所以接下來的例子都會以三顆為例子

How?
那接著會簡單講一下他是怎麼做到所謂的高可用性，或是說怎麼讓你的服務永遠不下線，
這邊舉一個簡單的例子，現在有一個3顆mongo組成的replicaset，一主二從，突然primary所在的這台server的機房突然停電，或是他故障了，那這時這兩個secondary突然發現 咦?要同步的主節點怎麼不見了 連不到了，那這時他們就會有人發起所謂的選舉，來選出新的primary，因此假設這個點選舉成功了，他就會成為新的primary，application又可以繼續連到了，而整個過程從發現primary不見倒選舉出新的primary的間隔時間非常的短，預設大概是12秒的時間，所以其實算是非常快就自動休好惹，就可能使用者正打電話給你說他壞掉啦 的時候 他又好惹 
那當然他的選舉機制的演算法認真要講的話也是比較複雜的，所以後面冠翰會再跟大家講解比較細的選舉機制

Read preference



Read concern
那講完剛剛的read preference後 我們可以知道說在replicaset的架構下，讀跟寫可能會發生在不同的mongodb，因為寫一定是發生在primary，而讀的話就不一定了，所以在這種情況下要怎麼保證我讀到的資料未來一定存在，或是要怎麼保證讀到的資料一定是最新寫入的資料，所以就有了read concern可以讓使用者根據自己的使用情境選擇適合的read concern
主要以下會分成四種
	local/available 
	majority
	linearizable
	 

Write concern
那接下來要講的是write concern，他是MongoDB寫入安全機制，跟剛剛的read concern一樣是一種客戶端設定，用於控制寫入安全的級別
主要就是說當有資料要被寫入時，怎樣才會被mongodb認為是成功的寫入，以下就分為三種level，分別是
	Majority
	Number
	Tag

Sync
接下來要來講secondary怎麼同步到primary的資料(加三個node旁邊有oplog的圖)

Oplog


Helm

production

