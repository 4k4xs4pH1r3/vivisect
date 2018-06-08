# APIs for Windows 64-bit MSVC 2008 runtime library (msvcr90).
# Built as a delta from the 32-bit version.
# Format:  retval, rettype, callconv, exactname, arglist(type, name)
#          arglist type is one of ['int', 'void *']
#          arglist name is one of [None, 'funcptr', 'obj', 'ptr']

# List the normalized name of any 32-bit functions to omit.
api_32_omits = [
    'msvcr90.??2@yapaxi@z',
    'msvcr90.??_u@yapaxi@z',
    'msvcr90.??3@yaxpax@z',
    'msvcr90.??_v@yaxpax@z'
]

# Define any functions specific to 64-bit.
api_64_adds = {
    'msvcr90.??2@yapeax_k@z':( 'int', None, 'cdecl', 'msvcr90.??2@YAPEAX_K@Z', (('int', None),) ),
    'msvcr90.??_u@yapeax_k@z':( 'int', None, 'cdecl', 'msvcr90.??_U@YAPEAX_K@Z', (('int', None),) ),
    'msvcr90.??3@yaxpeax@z':( 'void', None, 'cdecl', 'msvcr90.??3@YAXPEAX@Z', (('void *', 'ptr'),) ),
    'msvcr90.??_v@yaxpeax@z':( 'void', None, 'cdecl', 'msvcr90.??_V@YAXPEAX@Z', (('void *', 'ptr'),) ),
    }


# Build from the 32-bit API, skipping omits, changing the calling convention,
# and adding any specific 64-bit functions.
api_defs_64 = {}

import vivisect.impapi.windows.msvcr90_32 as m32
for name in m32.api_defs.iterkeys():
    if name in api_32_omits:
        continue
    (rtype,rname,cconv,cname,cargs) = m32.api_defs[name]
    api_defs_64[name] = (rtype, rname, 'msx64call', cname, cargs)
api_defs_64.update(api_64_adds)
