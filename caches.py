#Sai Ram
from m5.objects import Cache # cache is inherited from a class "BaseCache"

#Lets name the newcache as L1 cache and start by making L1 Cache class
class L1Cache(Cache):
	assoc=4
	tag_latency=2
	data_latency=2
	response_latency=2
	mshrs=4
	tgts_per_mshr=20

	def connectCPU(self, cpu):
		#need to define this in a base class!
		raise NotImplementedError

	def connectBus(self, bus):
		self.mem_side = bus.slave


#class L1ICache(L1Cache):
#	size='16KB'

#class L1DCache(L1Cache):
#	size='64KB'

class L2Cache(Cache):
	size='512kB'
	assoc=8
	tag_latency=20
	data_latency=20
	response_latency=20
	mshrs=20
	tgts_per_mshr=12
	
	def connectCPUSideBus(self, bus):
		self.cpu_side=bus.master
	
	def connectMemSideBus(self, bus):
		self.mem_side=bus.slave

#Now we have specified all the basic parameters for the BaseCache now we need to instantiate our subclasses and connect the caches to the interconnect

#To make out job neat we shall first write some helper functions
#Now we need to define a seperate connectCPU function for the datacaches and instruction caches since the I-cache and D-cache ports have a different names.

class L1ICache(L1Cache):
	size='64kB'
	
	def connectCPU(self, cpu):
		self.cpu_side=cpu.icache_port

class L1DCache(L1Cache):
	size='64kB'

	def connectCPU(self, cpu):
		self.cpu_side=cpu.dcache_port

